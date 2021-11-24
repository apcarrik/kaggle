def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[7]<=2:
		# {"feature": "Passanger", "instances": 19, "metric_value": 0.8315, "depth": 2}
		if obj[0]<=2:
			return 'True'
		elif obj[0]>2:
			# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[2]>0:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[1]>0:
					# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=9:
						return 'False'
					elif obj[3]>9:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[7]>2:
		return 'False'
	else: return 'False'
