def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[11]<=2:
		# {"feature": "Coffeehouse", "instances": 20, "metric_value": 1.0, "depth": 2}
		if obj[8]>1.0:
			# {"feature": "Time", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Age", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[4]<=5:
					# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[0]>1:
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]>0:
									return 'True'
								elif obj[5]<=0:
									return 'False'
								else: return 'False'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						elif obj[3]>0:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				elif obj[4]>5:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[8]<=1.0:
			# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[10]<=0:
				return 'False'
			elif obj[10]>0:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[11]>2:
		return 'False'
	else: return 'False'
