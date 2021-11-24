def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[10]<=3.0:
		# {"feature": "Time", "instances": 30, "metric_value": 0.9481, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Coupon", "instances": 19, "metric_value": 0.998, "depth": 3}
			if obj[2]>1:
				# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.9887, "depth": 4}
				if obj[11]<=1.0:
					# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[7]>1:
						# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[13]>1:
							# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[0]<=2:
								return 'False'
							elif obj[0]>2:
								# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]<=0:
									return 'False'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[13]<=1:
							# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[6]>1:
								# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[9]<=1.0:
									return 'False'
								elif obj[9]>1.0:
									return 'True'
								else: return 'True'
							elif obj[6]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[7]<=1:
						return 'True'
					else: return 'True'
				elif obj[11]>1.0:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		elif obj[1]>2:
			# {"feature": "Distance", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[13]>1:
				return 'True'
			elif obj[13]<=1:
				# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=3:
					return 'True'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[10]>3.0:
		return 'False'
	else: return 'False'
