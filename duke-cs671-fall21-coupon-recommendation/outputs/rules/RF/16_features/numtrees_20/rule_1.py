def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[12]<=1.0:
		# {"feature": "Coupon", "instances": 28, "metric_value": 0.9403, "depth": 2}
		if obj[3]>0:
			# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 3}
			if obj[9]<=7:
				# {"feature": "Time", "instances": 18, "metric_value": 0.9911, "depth": 4}
				if obj[2]>1:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[11]<=2.0:
						# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[13]<=1.0:
							return 'True'
						elif obj[13]>1.0:
							return 'False'
						else: return 'False'
					elif obj[11]>2.0:
						return 'False'
					else: return 'False'
				elif obj[2]<=1:
					# {"feature": "Age", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[6]>0:
						# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[5]>0:
							# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[11]<=0.0:
								return 'True'
							elif obj[11]>0.0:
								return 'False'
							else: return 'False'
						elif obj[5]<=0:
							return 'False'
						else: return 'False'
					elif obj[6]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[9]>7:
				return 'False'
			else: return 'False'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	elif obj[12]>1.0:
		# {"feature": "Education", "instances": 23, "metric_value": 0.8281, "depth": 2}
		if obj[8]<=2:
			# {"feature": "Coupon_validity", "instances": 15, "metric_value": 0.5665, "depth": 3}
			if obj[4]>0:
				return 'True'
			elif obj[4]<=0:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[3]>2:
					return 'True'
				elif obj[3]<=2:
					# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[7]<=0:
						return 'False'
					elif obj[7]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[8]>2:
			# {"feature": "Coupon_validity", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[4]>0:
				# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[11]<=1.0:
					return 'True'
				elif obj[11]>1.0:
					return 'False'
				else: return 'False'
			elif obj[4]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
