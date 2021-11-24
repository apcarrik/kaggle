def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[3]<=17:
		# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Passanger", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[5]>1:
					return 'True'
				elif obj[5]<=1:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=4:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]>1.0:
			# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>3:
					return 'True'
				elif obj[1]<=3:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[3]>17:
		return 'True'
	else: return 'True'
