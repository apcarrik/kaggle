def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]>0:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.9852, "depth": 2}
		if obj[3]>1:
			# {"feature": "Bar", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=2.0:
				# {"feature": "Direction_same", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]>2:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									return 'True'
								else: return 'True'
							elif obj[1]<=2:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[5]>1.0:
						return 'False'
					else: return 'False'
				elif obj[6]>0:
					return 'False'
				else: return 'False'
			elif obj[4]>2.0:
				return 'True'
			else: return 'True'
		elif obj[3]<=1:
			return 'True'
		else: return 'True'
	elif obj[2]<=0:
		# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[1]>0:
			return 'True'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=2:
				return 'False'
			elif obj[3]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
