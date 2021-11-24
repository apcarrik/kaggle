def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[7]<=11:
			# {"feature": "Education", "instances": 27, "metric_value": 0.999, "depth": 3}
			if obj[6]>1:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[2]>1:
					# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[12]<=0:
						# {"feature": "Income", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[8]>3:
							# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[4]>1:
									return 'False'
								elif obj[4]<=1:
									return 'True'
								else: return 'True'
							elif obj[3]>0:
								return 'True'
							else: return 'True'
						elif obj[8]<=3:
							return 'False'
						else: return 'False'
					elif obj[12]>0:
						return 'True'
					else: return 'True'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			elif obj[6]<=1:
				# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[10]<=1.0:
					# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[1]>2:
							return 'True'
						elif obj[1]<=2:
							# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[9]<=1.0:
									return 'True'
								elif obj[9]>1.0:
									return 'False'
								else: return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[10]>1.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[7]>11:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
