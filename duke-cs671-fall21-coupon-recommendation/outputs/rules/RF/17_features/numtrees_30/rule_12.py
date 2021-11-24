def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Maritalstatus", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[7]<=2:
		# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.9072, "depth": 2}
		if obj[14]<=1.0:
			# {"feature": "Time", "instances": 21, "metric_value": 0.9984, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[3]<=3:
					# {"feature": "Children", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[8]<=0:
						# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[4]>0:
							return 'False'
						elif obj[4]<=0:
							# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]>1:
								return 'True'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[8]>0:
						# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]>0:
								return 'False'
							elif obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[3]>3:
					return 'False'
				else: return 'False'
			elif obj[2]>1:
				# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[13]<=3.0:
					return 'True'
				elif obj[13]>3.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[14]>1.0:
			return 'True'
		else: return 'True'
	elif obj[7]>2:
		return 'False'
	else: return 'False'
