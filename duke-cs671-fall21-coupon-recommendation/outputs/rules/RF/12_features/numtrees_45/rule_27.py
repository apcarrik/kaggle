def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[11]<=2:
		# {"feature": "Age", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[4]>0:
			# {"feature": "Passanger", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[0]>0:
				# {"feature": "Gender", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[3]>0:
					# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[2]>1:
						# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[10]<=0:
							# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[1]<=2:
								return 'False'
							elif obj[1]>2:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]<=0:
									return 'False'
								elif obj[5]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[10]>0:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						return 'True'
					else: return 'True'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	elif obj[11]>2:
		return 'True'
	else: return 'True'
