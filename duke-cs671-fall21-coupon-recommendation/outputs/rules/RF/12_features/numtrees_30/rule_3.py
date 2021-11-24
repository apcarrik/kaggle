def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Bar", "instances": 23, "metric_value": 0.9656, "depth": 2}
		if obj[7]<=2.0:
			# {"feature": "Coupon", "instances": 19, "metric_value": 0.8315, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Distance", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[11]>1:
					# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[5]<=2:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=0:
								# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]>0:
									return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							elif obj[1]>0:
								return 'True'
							else: return 'True'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[11]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]>2:
				return 'False'
			else: return 'False'
		elif obj[7]>2.0:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
