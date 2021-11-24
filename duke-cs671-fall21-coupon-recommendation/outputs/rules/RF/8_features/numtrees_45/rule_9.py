def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[1]>2:
		# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.3712, "depth": 2}
		if obj[5]>1.0:
			return 'True'
		elif obj[5]<=1.0:
			# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[1]<=2:
		# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 2}
		if obj[7]>1:
			# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[3]>1:
				return 'False'
			elif obj[3]<=1:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=1:
					return 'False'
				elif obj[2]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[7]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
