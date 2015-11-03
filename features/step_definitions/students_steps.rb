Given(/^a "([^"]*)"\.$/) do |arg1|
  @input = arg1
  #puts @input
end

When(/^the converter is run\.$/) do
  @output = `python cucStudentList.py #{@input}`
  raise('Command Failed!') unless $?.success?
end

When(/^the converter is activated\.$/) do
  @output = `python cucConverter.py #{@input}`
  raise('Command Failed!') unless $?.success?
end

When(/^we press go\.$/) do
  @output = `python cucProfList.py #{@input}`
  raise('Command Failed!') unless $?.success?
end

When(/^we hit the button\.$/) do
  @output = `python cucSchedule.py #{@input}`
  raise('Command Failed!') unless $?.success?
end

When(/^we make it go\.$/) do
  @output = `python cucConflicts.py #{@input}`
  raise('Command Failed!') unless $?.success?
end

Then(/^the output should be "([^"]*)"\.$/) do |arg1|
  expect(arg1).to eq(@output)
end
