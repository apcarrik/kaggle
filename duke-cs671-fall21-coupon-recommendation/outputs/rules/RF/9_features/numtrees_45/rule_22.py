def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[4]<=11:
		# {"feature": "Education", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[3]<=3:
			# {"feature": "Coupon", "instances": 16, "metric_value": 1.0, "depth": 3}
			if obj[2]>0:
				# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9852, "depth": 4}
				if obj[6]>0.0:
					# {"feature": "Passanger", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Bar", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									return 'True'
								else: return 'True'
							elif obj[5]>0.0:
								return 'True'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8]>1:
									return 'True'
								elif obj[8]<=1:
									return 'False'
								else: return 'False'
							elif obj[5]>1.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[6]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[3]>3:
			return 'True'
		else: return 'True'
	elif obj[4]>11:
		return 'True'
	else: return 'True'
