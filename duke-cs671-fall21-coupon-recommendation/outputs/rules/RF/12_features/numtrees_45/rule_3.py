def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.3712, "depth": 2}
		if obj[6]<=11:
			return 'True'
		elif obj[6]>11:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 2}
		if obj[11]<=2:
			# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[3]>0:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=2:
					return 'False'
				elif obj[5]>2:
					return 'True'
				else: return 'True'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		elif obj[11]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
