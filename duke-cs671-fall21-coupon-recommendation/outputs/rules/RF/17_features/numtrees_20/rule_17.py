def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon_validity", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[4]<=0:
		# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.8366, "depth": 2}
		if obj[14]<=1.0:
			# {"feature": "Distance", "instances": 22, "metric_value": 0.9457, "depth": 3}
			if obj[16]<=2:
				# {"feature": "Education", "instances": 19, "metric_value": 0.8315, "depth": 4}
				if obj[9]>0:
					# {"feature": "Occupation", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[10]>3:
						# {"feature": "Time", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 7}
							if obj[3]>0:
								return 'True'
							elif obj[3]<=0:
								return 'False'
							else: return 'False'
						elif obj[2]>3:
							return 'False'
						else: return 'False'
					elif obj[10]<=3:
						return 'False'
					else: return 'False'
				elif obj[9]<=0:
					return 'True'
				else: return 'True'
			elif obj[16]>2:
				return 'False'
			else: return 'False'
		elif obj[14]>1.0:
			return 'True'
		else: return 'True'
	elif obj[4]>0:
		# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.9183, "depth": 2}
		if obj[13]<=2.0:
			# {"feature": "Weather", "instances": 17, "metric_value": 0.9774, "depth": 3}
			if obj[1]<=0:
				# {"feature": "Occupation", "instances": 14, "metric_value": 1.0, "depth": 4}
				if obj[10]>5:
					# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[6]<=2:
						return 'False'
					elif obj[6]>2:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[9]<=0:
							return 'True'
						elif obj[9]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[10]<=5:
					# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[9]>1:
						return 'True'
					elif obj[9]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		elif obj[13]>2.0:
			return 'False'
		else: return 'False'
	else: return 'False'
