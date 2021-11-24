def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Direction_same", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[7]<=0:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[4]>3:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[6]>0.0:
					# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[3]>1:
						# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[0]>1:
								# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[2]<=2:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						elif obj[5]>0.0:
							return 'False'
						else: return 'False'
					elif obj[3]<=1:
						return 'True'
					else: return 'True'
				elif obj[6]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[4]<=3:
				return 'False'
			else: return 'False'
		elif obj[7]>0:
			return 'True'
		else: return 'True'
	elif obj[1]>3:
		return 'False'
	else: return 'False'
