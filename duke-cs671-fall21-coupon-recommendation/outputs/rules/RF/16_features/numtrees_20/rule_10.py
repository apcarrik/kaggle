def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[8]<=1:
		# {"feature": "Distance", "instances": 29, "metric_value": 0.9294, "depth": 2}
		if obj[15]<=2:
			# {"feature": "Income", "instances": 26, "metric_value": 0.8404, "depth": 3}
			if obj[10]>2:
				# {"feature": "Age", "instances": 20, "metric_value": 0.9341, "depth": 4}
				if obj[6]>2:
					# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[12]<=3.0:
						# {"feature": "Bar", "instances": 11, "metric_value": 0.4395, "depth": 6}
						if obj[11]<=2.0:
							return 'True'
						elif obj[11]>2.0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[12]>3.0:
						return 'False'
					else: return 'False'
				elif obj[6]<=2:
					# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[9]>3:
						return 'False'
					elif obj[9]<=3:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[10]<=2:
				return 'True'
			else: return 'True'
		elif obj[15]>2:
			return 'False'
		else: return 'False'
	elif obj[8]>1:
		# {"feature": "Income", "instances": 22, "metric_value": 0.684, "depth": 2}
		if obj[10]<=6:
			# {"feature": "Age", "instances": 18, "metric_value": 0.3095, "depth": 3}
			if obj[6]>0:
				return 'False'
			elif obj[6]<=0:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=0:
					return 'False'
				elif obj[2]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]>6:
			# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
