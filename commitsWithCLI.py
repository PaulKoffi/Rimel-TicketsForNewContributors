import requests 
import json 
import argparse
import os.path


def getLastPageOfCommitsOfAContributor(ownerArg, repoArg, nameArg):
    response = requests.get('https://api.github.com/repos/{owner}/{repo}/commits?author={author}'.format(owner= ownerArg, repo=repoArg, author=nameArg))
    links = response.headers['Link']

    linksSplitted = links.split(',')

    indexTopage = linksSplitted[1].find('page')

    index = indexTopage + 5
    pageNumber = ''
    while linksSplitted[1][index].isnumeric():
        pageNumber += linksSplitted[1][index]
        index += 1

    return pageNumber

# def pardingMessage (message, )
def getNumberOfLabelsWhenItsUsed(ownerArg, repoArg, nameArg):
    infosCommits = {
        'nombreTotalDeCommitsAnalyses' : 0,
        'nombreDeCommitsEtiquettesAnalyses' : 0,
        'nombreDeCommitsNonEtiquettesAnalyses' : 0
    }
    infosIssues = {
        'nombreTotalIssuesAnalysees' : 0,
        'nombreIssuesLabelisees' : 0,
        'nombreIssuesNonLabelisees' : 0,
        'nombreIssuesNonLabeliseesQuiReference': 0
    }
    labels = {}
    pageNumber = getLastPageOfCommitsOfAContributor(ownerArg, repoArg, nameArg)
    for i in range (0,3):

        convertedPageNumberToInt = int(pageNumber) - i
        convertedPageNumberIntToString = str(convertedPageNumberToInt)
        print(convertedPageNumberIntToString)
        response1 = requests.get('https://api.github.com/repos/{owner}/{repo}/commits?author={author}&page={pageNumber}'.format(owner=ownerArg, repo=repoArg, author=nameArg,pageNumber=convertedPageNumberIntToString))

        commits = response1.json()

        for commit in commits :
            infosCommits['nombreTotalDeCommitsAnalyses'] += 1  
            commitMessage = commit['commit']['message']
            indexToHashtag = commitMessage.find('#')
            if indexToHashtag != -1:
                infosCommits['nombreDeCommitsEtiquettesAnalyses'] += 1
                infosIssues['nombreTotalIssuesAnalysees'] += 1 
                issueNumber = ''
                index1 = indexToHashtag 
                while index1 < len(commitMessage) - 1 and commitMessage[index1 + 1].isnumeric():
                    issueNumber += commitMessage[index1 + 1]
                    index1 += 1

                response2 = requests.get('https://api.github.com/repos/{owner}/{repo}/issues/{issueNumber}'.format(owner='microsoft', repo='vscode',issueNumber=issueNumber))

                # issueLabels = response2.json()['labels'] if 'labels' in response2.json() else []
                issueBody = response2.json()['body'] if 'body' in response2.json() else ""
                indexToHashtagIssue = issueBody.find("#")
                if 'labels' in response2.json():
                    issueLabels = response2.json()['labels']
                    infosIssues['nombreIssuesLabelisees'] += 1

                elif indexToHashtagIssue != -1:
                    infosIssues['nombreIssuesNonLabeliseesQuiReference'] += 1
                    issueNumber = ''
                    index1 = indexToHashtagIssue 
                    while index1 < len(issueBody) - 1 and issueBody[index1 + 1].isnumeric():
                        issueNumber += issueBody[index1 + 1]
                        index1 += 1

                    response3 = requests.get('https://api.github.com/repos/{owner}/{repo}/issues/{issueNumber}'.format(owner='microsoft', repo='vscode',issueNumber=issueNumber))
                    if 'labels' in response3.json():
                        issueLabels = response3.json()['labels']
                        infosIssues['nombreIssuesLabelisees'] += 1
                    else:
                        issueLabels = []
                        infosIssues['nombreIssuesNonLabelisees'] += 1

                else:
                    issueLabels = []
                    infosIssues['nombreIssuesNonLabelisees'] += 1

                for label in issueLabels:
                    if 'name' in label:
                        if label['name'] not in labels:
                            labels[label['name']] = 1
                        else:
                            labels[label['name']] += 1
            else:
                infosCommits['nombreDeCommitsNonEtiquettesAnalyses'] += 1 
    # print(labels)
    return { 'infosCommits': infosCommits , 'infosIssues': infosIssues, 'labels': labels }

def writeToAJsonFile(ownerArg, repoArg,result):
    if os.path.isfile("results/{}-{}.json".format(ownerArg,repoArg)):
        with open("results/{}-{}.json".format(ownerArg,repoArg),"r") as outfile:
            oldResult = json.loads(outfile.read())
            for infosCommitsKey in result['infosCommits']:
                result['infosCommits'][infosCommitsKey] += oldResult['infosCommits'][infosCommitsKey]
            
            for labelsKey in oldResult['labels']:
                if labelsKey in result['labels']:
                    result['labels'][labelsKey] += oldResult['labels'][labelsKey]
                else:
                    result['labels'][labelsKey] = oldResult['labels'][labelsKey]

            for infosIssuesKey in result['infosIssues']:
                result['infosIssues'][infosIssuesKey] += oldResult['infosIssues'][infosIssuesKey]
        
        lastUpdate = result

        with open("results/{}-{}.json".format(ownerArg,repoArg),"w") as outfile:
            json_object = json.dumps(lastUpdate, indent=4)
            outfile.write(json_object)
    else: 
        with open("results/{}-{}.json".format(ownerArg,repoArg),"w") as outfile:
            json_object = json.dumps(result, indent=4)
            outfile.write(json_object)


#--------------------------------------------------------------------------------#
parser = argparse.ArgumentParser()

parser.add_argument('-o','--owner', help='The name of the organization')
parser.add_argument('-r', '--repo', help='The name of the repository')
parser.add_argument('-n', '--name', help='The name of the contributors')

args = parser.parse_args()

if args.owner and args.repo and args.name:
    print("Displaying Owner as : % s" % args.owner)
    print("Displaying Owner as : % s" % args.repo)
    print("Displaying Owner as : % s" % args.name)

    labels = getNumberOfLabelsWhenItsUsed(args.owner, args.repo, args.name)
    writeToAJsonFile(args.owner, args.repo,labels)