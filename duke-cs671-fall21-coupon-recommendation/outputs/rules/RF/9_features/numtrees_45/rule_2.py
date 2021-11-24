def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[4]<=11:
			# {"feature": "Bar", "instances": 16, "metric_value": 0.896, "depth": 3}
			if obj[5]<=0.0:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[2]>0:
					# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[1]>0:
								return 'True'
							elif obj[1]<=0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]>2.0:
							return 'False'
						else: return 'False'
					elif obj[3]>2:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[5]>0.0:
				return 'False'
			else: return 'False'
		elif obj[4]>11:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
