def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[5]>4:
			return 'True'
		elif obj[5]<=4:
			# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[4]>1:
				return 'False'
			elif obj[4]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[3]<=2:
			return 'False'
		elif obj[3]>2:
			# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=2:
				return 'True'
			elif obj[2]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
