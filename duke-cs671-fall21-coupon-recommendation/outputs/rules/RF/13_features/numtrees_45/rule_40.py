def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Children", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[5]>0:
		# {"feature": "Passanger", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[0]>1:
			# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[8]<=0.0:
				# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[9]>0.0:
					return 'True'
				elif obj[9]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[8]>0.0:
				return 'False'
			else: return 'False'
		elif obj[0]<=1:
			return 'False'
		else: return 'False'
	elif obj[5]<=0:
		# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[4]<=5:
			return 'True'
		elif obj[4]>5:
			return 'False'
		else: return 'False'
	else: return 'True'
