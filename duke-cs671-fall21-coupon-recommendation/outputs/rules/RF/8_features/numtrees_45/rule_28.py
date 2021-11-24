def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[1]>0:
		# {"feature": "Passanger", "instances": 14, "metric_value": 1.0, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[3]<=17:
				# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[7]<=1:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]>0:
									return 'True'
								elif obj[2]<=0:
									return 'True'
								else: return 'True'
							elif obj[6]>0:
								return 'False'
							else: return 'False'
						elif obj[7]>1:
							return 'False'
						else: return 'False'
					elif obj[5]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[3]>17:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	elif obj[1]<=0:
		return 'False'
	else: return 'False'
