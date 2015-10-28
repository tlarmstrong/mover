Given(/^a "([^"]*)"\.$/) do |arg1|
  @input = arg1
  #puts @input
end

When(/^the finder is run\.$/) do
  @output = `python mockStudentList.py #{@input}`
  raise('Command Failed!') unless $?.success?
end

When(/^the converter is run\.$/) do
  @output = `python mockStudentList.py #{@input}`
  raise('Command Failed!') unless $?.success?
end


Then(/^the output should be "([^"]*)"\.$/) do |arg1|
  expect(arg1).to eq(@output)
end
