def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[2]>0:
		# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.9666, "depth": 2}
		if obj[9]<=2.0:
			# {"feature": "Occupation", "instances": 23, "metric_value": 0.8865, "depth": 3}
			if obj[7]<=14:
				# {"feature": "Time", "instances": 21, "metric_value": 0.7919, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Distance", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[12]>1:
						# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[10]<=1.0:
							# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[4]<=3:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[0]>1:
									return 'False'
								elif obj[0]<=1:
									# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[6]>1:
										return 'False'
									elif obj[6]<=1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[4]>3:
								return 'True'
							else: return 'True'
						elif obj[10]>1.0:
							return 'False'
						else: return 'False'
					elif obj[12]<=1:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[7]>14:
				return 'False'
			else: return 'False'
		elif obj[9]>2.0:
			# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[5]>0:
				return 'False'
			elif obj[5]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
