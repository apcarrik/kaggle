def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[4]>0:
		# {"feature": "Age", "instances": 16, "metric_value": 1.0, "depth": 2}
		if obj[3]<=4:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[5]<=15:
				# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[8]>0.0:
					# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[6]>0.0:
							# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[7]>0.0:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[2]>0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=1:
											# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[2]<=0:
										return 'False'
									else: return 'False'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							elif obj[7]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[6]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[8]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[5]>15:
				return 'False'
			else: return 'False'
		elif obj[3]>4:
			return 'False'
		else: return 'False'
	elif obj[4]<=0:
		return 'True'
	else: return 'True'
