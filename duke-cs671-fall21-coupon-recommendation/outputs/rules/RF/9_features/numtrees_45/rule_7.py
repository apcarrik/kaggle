def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Bar", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[5]>0.0:
			# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[8]<=1:
				# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[6]<=2.0:
					return 'True'
				elif obj[6]>2.0:
					return 'False'
				else: return 'False'
			elif obj[8]>1:
				return 'False'
			else: return 'False'
		elif obj[5]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[1]>1:
		# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[3]<=3:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[4]<=13:
				return 'True'
			elif obj[4]>13:
				return 'False'
			else: return 'False'
		elif obj[3]>3:
			return 'False'
		else: return 'False'
	else: return 'True'
