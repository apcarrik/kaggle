def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.8974, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 41, "metric_value": 0.965, "depth": 2}
		if obj[10]>1:
			# {"feature": "Coupon_validity", "instances": 36, "metric_value": 0.9911, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Coupon", "instances": 23, "metric_value": 0.8865, "depth": 4}
				if obj[3]<=1:
					# {"feature": "Age", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[6]>1:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[14]<=2.0:
							return 'False'
						elif obj[14]>2.0:
							return 'True'
						else: return 'True'
					elif obj[6]<=1:
						# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[11]<=5:
							return 'True'
						elif obj[11]>5:
							# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[7]<=1:
								return 'False'
							elif obj[7]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			elif obj[4]>0:
				# {"feature": "Maritalstatus", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[7]<=1:
					# {"feature": "Gender", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[5]<=0:
						return 'False'
					elif obj[5]>0:
						# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=0:
							return 'True'
						elif obj[1]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[7]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]<=1:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
