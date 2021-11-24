def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 18, "metric_value": 0.3095, "depth": 2}
		if obj[5]<=2:
			return 'True'
		elif obj[5]>2:
			# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Distance", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[11]<=1:
			# {"feature": "Gender", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[3]<=0:
				# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[4]>0:
					return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]>0:
				return 'True'
			else: return 'True'
		elif obj[11]>1:
			return 'False'
		else: return 'False'
	else: return 'False'
