def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 30, "metric_value": 0.9968, "depth": 2}
		if obj[7]>1:
			# {"feature": "Education", "instances": 26, "metric_value": 0.9612, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Income", "instances": 19, "metric_value": 0.998, "depth": 4}
				if obj[8]>5:
					# {"feature": "Coupon", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[2]>3:
						# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[9]>0.0:
							# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[3]<=0:
								return 'False'
							elif obj[3]>0:
								return 'True'
							else: return 'True'
						elif obj[9]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[2]<=3:
						return 'True'
					else: return 'True'
				elif obj[8]<=5:
					# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]>2:
				return 'False'
			else: return 'False'
		elif obj[7]<=1:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Distance", "instances": 21, "metric_value": 0.4537, "depth": 2}
		if obj[13]>1:
			return 'True'
		elif obj[13]<=1:
			# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[2]>2:
				return 'True'
			elif obj[2]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
