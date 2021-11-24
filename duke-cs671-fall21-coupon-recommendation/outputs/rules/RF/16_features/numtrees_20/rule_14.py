def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[15]>1:
		# {"feature": "Education", "instances": 28, "metric_value": 0.9852, "depth": 2}
		if obj[8]>1:
			# {"feature": "Income", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[10]>2:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[13]>1.0:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=2:
						return 'False'
					elif obj[3]>2:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>0:
								return 'False'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[13]<=1.0:
					return 'True'
				else: return 'True'
			elif obj[10]<=2:
				return 'False'
			else: return 'False'
		elif obj[8]<=1:
			# {"feature": "Children", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[7]>0:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[9]>1:
					return 'True'
				elif obj[9]<=1:
					# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]<=0:
				# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[13]<=1.0:
					return 'False'
				elif obj[13]>1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[15]<=1:
		# {"feature": "Bar", "instances": 23, "metric_value": 0.7554, "depth": 2}
		if obj[11]<=1.0:
			# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.4855, "depth": 3}
			if obj[13]>0.0:
				return 'True'
			elif obj[13]<=0.0:
				# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[2]<=1:
					return 'True'
				elif obj[2]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[11]>1.0:
			# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[3]>2:
				return 'False'
			elif obj[3]<=2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
