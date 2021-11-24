def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[3]>1:
		# {"feature": "Coupon_validity", "instances": 64, "metric_value": 0.9422, "depth": 2}
		if obj[4]<=0:
			# {"feature": "Age", "instances": 35, "metric_value": 0.7755, "depth": 3}
			if obj[6]>2:
				# {"feature": "Passanger", "instances": 20, "metric_value": 0.971, "depth": 4}
				if obj[0]>1:
					# {"feature": "Occupation", "instances": 12, "metric_value": 0.4138, "depth": 5}
					if obj[10]<=9:
						return 'True'
					elif obj[10]>9:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>2:
							return 'True'
						elif obj[2]<=2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[0]<=1:
					# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[9]<=2:
						return 'False'
					elif obj[9]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]<=2:
				return 'True'
			else: return 'True'
		elif obj[4]>0:
			# {"feature": "Passanger", "instances": 29, "metric_value": 0.9991, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Weather", "instances": 20, "metric_value": 0.9341, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Time", "instances": 18, "metric_value": 0.8524, "depth": 5}
					if obj[2]<=1:
						# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[9]>0:
							# {"feature": "Children", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[8]<=0:
								return 'False'
							elif obj[8]>0:
								return 'True'
							else: return 'True'
						elif obj[9]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]>1:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Weather", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[3]<=1:
		# {"feature": "Bar", "instances": 21, "metric_value": 0.9183, "depth": 2}
		if obj[12]<=1.0:
			# {"feature": "Coupon_validity", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[4]<=0:
				return 'False'
			elif obj[4]>0:
				# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[9]>1:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[9]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[12]>1.0:
			# {"feature": "Coupon_validity", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
