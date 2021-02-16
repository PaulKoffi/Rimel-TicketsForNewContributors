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


def getNumberOfLabelsWhenItsUsed(ownerArg, repoArg, nameArg):
    labels = {}
    pageNumber = getLastPageOfCommitsOfAContributor(ownerArg, repoArg, nameArg)
    for i in range (0,3):

        convertedPageNumberToInt = int(pageNumber) - i
        convertedPageNumberIntToString = str(convertedPageNumberToInt)
        print(convertedPageNumberIntToString)
        response1 = requests.get('https://api.github.com/repos/{owner}/{repo}/commits?author={author}&page={pageNumber}'.format(owner=ownerArg, repo=repoArg, author=nameArg,pageNumber=convertedPageNumberIntToString))

        commits = response1.json()

        for commit in commits :
            commitMessage = commit['commit']['message']
            indexToHastag = commitMessage.find('#')
            if indexToHastag != -1:
                issueNumber = ''
                index1 = indexToHastag 
                while index1 < len(commitMessage) - 1 and commitMessage[index1 + 1].isnumeric():
                    issueNumber += commitMessage[index1 + 1]
                    index1 += 1

                response2 = requests.get('https://api.github.com/repos/{owner}/{repo}/issues/{issueNumber}'.format(owner='microsoft', repo='vscode',issueNumber=issueNumber))

                issueLabels = response2.json()['labels'] if 'labels' in response2.json() else []
                
                for label in issueLabels:
                    if 'name' in label:
                        if label['name'] not in labels:
                            labels[label['name']] = 1
                        else:
                            labels[label['name']] += 1

    # print(labels)
    return labels

def writeToAJsonFile(ownerArg, repoArg,labels):
    if os.path.isFile("{}-{}.json".format(ownerArg,repoArg)):
        with open("{}-{}.json".format(ownerArg,repoArg),"r") as outfile:
            oldLabels = json.loads(outfile)
            print(oldLabels)
            for labelKey in labels:
                oldLabels[labelKey] += labels[labelKey]
    # json_object = json.dumps(labels, indent=4)


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