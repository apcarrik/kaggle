def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[1]>1:
		# {"feature": "Education", "instances": 16, "metric_value": 0.9887, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Direction_same", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[6]<=0:
				# {"feature": "Distance", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[7]<=2:
					return 'True'
				elif obj[7]>2:
					return 'False'
				else: return 'False'
			elif obj[6]>0:
				return 'False'
			else: return 'False'
		elif obj[2]>2:
			return 'False'
		else: return 'False'
	elif obj[1]<=1:
		return 'False'
	else: return 'False'
