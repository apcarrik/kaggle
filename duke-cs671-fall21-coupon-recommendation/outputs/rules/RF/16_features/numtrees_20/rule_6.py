def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Weather", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Passanger", "instances": 46, "metric_value": 0.9945, "depth": 2}
		if obj[0]>0:
			# {"feature": "Occupation", "instances": 43, "metric_value": 0.9808, "depth": 3}
			if obj[9]<=7:
				# {"feature": "Gender", "instances": 25, "metric_value": 0.9896, "depth": 4}
				if obj[5]>0:
					# {"feature": "Time", "instances": 14, "metric_value": 0.7496, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Income", "instances": 11, "metric_value": 0.4395, "depth": 6}
						if obj[10]>0:
							return 'False'
						elif obj[10]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[10]>1:
							return 'True'
						elif obj[10]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]<=0:
					# {"feature": "Coupon", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[2]>0:
							# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[10]<=7:
								return 'False'
							elif obj[10]>7:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[3]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[9]>7:
				# {"feature": "Bar", "instances": 18, "metric_value": 0.7642, "depth": 4}
				if obj[11]>0.0:
					# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[8]>1:
						# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[6]>1:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[13]<=1.0:
								return 'True'
							elif obj[13]>1.0:
								return 'False'
							else: return 'False'
						elif obj[6]<=1:
							return 'True'
						else: return 'True'
					elif obj[8]<=1:
						return 'False'
					else: return 'False'
				elif obj[11]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[1]>1:
		return 'False'
	else: return 'False'
