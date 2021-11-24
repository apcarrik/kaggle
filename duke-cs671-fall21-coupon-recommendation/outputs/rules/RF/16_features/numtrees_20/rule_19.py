def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[8]>1:
		# {"feature": "Coupon_validity", "instances": 29, "metric_value": 0.9923, "depth": 2}
		if obj[4]>0:
			# {"feature": "Children", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[7]>0:
				return 'False'
			elif obj[7]<=0:
				# {"feature": "Income", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[10]<=3:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[9]<=14:
						return 'True'
					elif obj[9]>14:
						return 'False'
					else: return 'False'
				elif obj[10]>3:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[4]<=0:
			# {"feature": "Income", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[10]>0:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[9]>6:
					# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=0:
						return 'True'
					elif obj[5]>0:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=1:
							return 'False'
						elif obj[6]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[9]<=6:
					return 'False'
				else: return 'False'
			elif obj[10]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[8]<=1:
		# {"feature": "Coupon", "instances": 22, "metric_value": 0.7732, "depth": 2}
		if obj[3]>0:
			# {"feature": "Income", "instances": 20, "metric_value": 0.6098, "depth": 3}
			if obj[10]<=6:
				# {"feature": "Time", "instances": 17, "metric_value": 0.3228, "depth": 4}
				if obj[2]<=3:
					return 'True'
				elif obj[2]>3:
					# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]>0:
						return 'True'
					elif obj[6]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[10]>6:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
