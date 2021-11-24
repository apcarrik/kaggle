def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[6]<=2.0:
		# {"feature": "Education", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[5]<=6:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[0]>1:
					# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[3]>0:
						# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1]<=0:
								return 'True'
							elif obj[1]>0:
								# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=2.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=2:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[0]<=1:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>6:
				return 'True'
			else: return 'True'
		elif obj[4]>2:
			# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=0:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[6]>2.0:
		return 'False'
	else: return 'False'
