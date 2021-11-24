def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[7]<=9:
			# {"feature": "Coupon", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[2]>1:
				# {"feature": "Age", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[4]>1:
					# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[10]<=1.0:
						# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[11]<=0:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[12]>1:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5]>0:
											return 'False'
										elif obj[5]<=0:
											return 'True'
										else: return 'True'
									elif obj[0]>2:
										return 'True'
									else: return 'True'
								elif obj[12]<=1:
									return 'False'
								else: return 'False'
							elif obj[11]>0:
								return 'False'
							else: return 'False'
						elif obj[3]>0:
							return 'False'
						else: return 'False'
					elif obj[10]>1.0:
						return 'True'
					else: return 'True'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		elif obj[7]>9:
			return 'False'
		else: return 'False'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
