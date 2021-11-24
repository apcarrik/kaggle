def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Direction_same", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[5]<=0:
		# {"feature": "Education", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[2]>1:
			# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[4]<=2.0:
				# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[1]>2:
					# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[3]>1:
							# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'True'
							else: return 'True'
						elif obj[3]<=1:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[1]<=2:
					return 'False'
				else: return 'False'
			elif obj[4]>2.0:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	elif obj[5]>0:
		return 'True'
	else: return 'True'
