def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[8]>1:
		# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 2}
		if obj[3]<=3:
			# {"feature": "Passanger", "instances": 21, "metric_value": 0.9984, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[2]>1:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[4]<=6:
							# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[1]>1:
									return 'False'
								elif obj[1]<=1:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]>1.0:
								return 'True'
							else: return 'True'
						elif obj[4]>6:
							return 'True'
						else: return 'True'
					elif obj[5]>1.0:
						return 'False'
					else: return 'False'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[3]>3:
			return 'True'
		else: return 'True'
	elif obj[8]<=1:
		return 'True'
	else: return 'True'
