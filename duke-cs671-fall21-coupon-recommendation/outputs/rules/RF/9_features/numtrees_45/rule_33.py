def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[4]>1:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[2]>0:
			# {"feature": "Education", "instances": 16, "metric_value": 1.0, "depth": 3}
			if obj[3]>0:
				# {"feature": "Passanger", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[6]<=2.0:
						# {"feature": "Bar", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[5]<=2.0:
							# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[8]>1:
								# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							elif obj[8]<=1:
								return 'True'
							else: return 'True'
						elif obj[5]>2.0:
							return 'True'
						else: return 'True'
					elif obj[6]>2.0:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					return 'False'
				else: return 'False'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[4]<=1:
		return 'True'
	else: return 'True'
