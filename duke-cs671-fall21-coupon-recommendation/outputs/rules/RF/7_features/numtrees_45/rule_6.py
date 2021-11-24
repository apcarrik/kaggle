def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[3]>1:
		# {"feature": "Direction_same", "instances": 14, "metric_value": 0.9852, "depth": 2}
		if obj[5]<=0:
			# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[6]>1:
				# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[4]>-1.0:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]<=1:
							return 'False'
						elif obj[2]>1:
							return 'True'
						else: return 'True'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[4]<=-1.0:
					return 'False'
				else: return 'False'
			elif obj[6]<=1:
				return 'False'
			else: return 'False'
		elif obj[5]>0:
			# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[4]<=1.0:
				return 'True'
			elif obj[4]>1.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=1:
		return 'True'
	else: return 'True'
