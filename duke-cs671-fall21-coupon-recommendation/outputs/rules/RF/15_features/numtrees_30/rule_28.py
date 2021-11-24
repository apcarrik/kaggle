def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[10]<=2.0:
		# {"feature": "Coupon", "instances": 30, "metric_value": 1.0, "depth": 2}
		if obj[2]>1:
			# {"feature": "Occupation", "instances": 25, "metric_value": 0.971, "depth": 3}
			if obj[8]<=9:
				# {"feature": "Children", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[6]>0:
					# {"feature": "Income", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[9]<=6:
						# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[4]>0:
								return 'False'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						elif obj[1]>1:
							# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[4]>0:
								return 'True'
							elif obj[4]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[9]>6:
						return 'True'
					else: return 'True'
				elif obj[6]<=0:
					return 'True'
				else: return 'True'
			elif obj[8]>9:
				# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[1]>1:
					# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[11]<=1.0:
						return 'False'
					elif obj[11]>1.0:
						return 'True'
					else: return 'True'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	elif obj[10]>2.0:
		return 'True'
	else: return 'True'
