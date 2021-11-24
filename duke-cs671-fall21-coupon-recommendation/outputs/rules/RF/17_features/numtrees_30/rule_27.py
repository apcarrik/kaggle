def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Income", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[11]>0:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.9923, "depth": 2}
		if obj[10]>1:
			# {"feature": "Distance", "instances": 25, "metric_value": 0.9988, "depth": 3}
			if obj[16]<=2:
				# {"feature": "Gender", "instances": 20, "metric_value": 0.971, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[14]>1.0:
						return 'True'
					elif obj[14]<=1.0:
						# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=5:
								return 'False'
							elif obj[6]>5:
								return 'True'
							else: return 'True'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[5]>0:
					# {"feature": "Age", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[6]<=3:
						# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[7]<=1:
								return 'True'
							elif obj[7]>1:
								return 'False'
							else: return 'False'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					elif obj[6]>3:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[16]>2:
				return 'False'
			else: return 'False'
		elif obj[10]<=1:
			return 'True'
		else: return 'True'
	elif obj[11]<=0:
		return 'False'
	else: return 'False'
