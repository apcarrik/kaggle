def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[4]<=14:
		# {"feature": "Time", "instances": 21, "metric_value": 0.9852, "depth": 2}
		if obj[1]>0:
			# {"feature": "Education", "instances": 18, "metric_value": 1.0, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.9887, "depth": 4}
				if obj[7]>0.0:
					# {"feature": "Bar", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[2]>0:
								return 'True'
							elif obj[2]<=0:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=2:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[6]>2.0:
							return 'False'
						else: return 'False'
					elif obj[5]<=0.0:
						# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[6]<=3.0:
							return 'False'
						elif obj[6]>3.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[7]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[3]>3:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[4]>14:
		return 'False'
	else: return 'False'
