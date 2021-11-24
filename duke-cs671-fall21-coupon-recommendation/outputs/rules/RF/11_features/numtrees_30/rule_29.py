def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[10]<=2:
		# {"feature": "Time", "instances": 29, "metric_value": 0.9991, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.9587, "depth": 3}
			if obj[5]>4:
				# {"feature": "Coupon", "instances": 16, "metric_value": 1.0, "depth": 4}
				if obj[2]>0:
					# {"feature": "Education", "instances": 15, "metric_value": 0.9968, "depth": 5}
					if obj[4]<=4:
						# {"feature": "Passanger", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[0]>0:
							# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 1.0, "depth": 7}
							if obj[8]<=1.0:
								# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[9]<=0:
									# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[6]<=2.0:
										return 'False'
									elif obj[6]>2.0:
										return 'True'
									else: return 'True'
								elif obj[9]>0:
									return 'True'
								else: return 'True'
							elif obj[8]>1.0:
								# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=1.0:
									return 'True'
								elif obj[6]>1.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[4]>4:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			elif obj[5]<=4:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[4]<=2:
				return 'True'
			elif obj[4]>2:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[10]>2:
		return 'False'
	else: return 'False'
