def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[4]<=12:
		# {"feature": "Passanger", "instances": 43, "metric_value": 0.9682, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Distance", "instances": 36, "metric_value": 0.9978, "depth": 3}
			if obj[9]>1:
				# {"feature": "Bar", "instances": 21, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=1.0:
					# {"feature": "Time", "instances": 15, "metric_value": 0.9968, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9612, "depth": 6}
						if obj[7]<=1.0:
							# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[6]<=3.0:
								# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[3]>0:
									# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[2]>0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[2]<=0:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							elif obj[6]>3.0:
								return 'False'
							else: return 'False'
						elif obj[7]>1.0:
							return 'False'
						else: return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[5]>1.0:
					return 'False'
				else: return 'False'
			elif obj[9]<=1:
				# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.7219, "depth": 4}
				if obj[6]>0.0:
					return 'True'
				elif obj[6]<=0.0:
					# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[7]>-1.0:
								return 'False'
							elif obj[7]<=-1.0:
								return 'True'
							else: return 'True'
						elif obj[5]>1.0:
							return 'True'
						else: return 'True'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	elif obj[4]>12:
		return 'False'
	else: return 'False'
