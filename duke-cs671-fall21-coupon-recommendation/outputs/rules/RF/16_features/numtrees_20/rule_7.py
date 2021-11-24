def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[9]<=10:
		# {"feature": "Coupon", "instances": 35, "metric_value": 0.9275, "depth": 2}
		if obj[3]>0:
			# {"feature": "Age", "instances": 31, "metric_value": 0.8238, "depth": 3}
			if obj[6]>1:
				# {"feature": "Bar", "instances": 19, "metric_value": 0.4855, "depth": 4}
				if obj[11]<=1.0:
					return 'True'
				elif obj[11]>1.0:
					# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4]>0:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=1:
							return 'False'
						elif obj[2]>1:
							return 'True'
						else: return 'True'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[6]<=1:
				# {"feature": "Weather", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Gender", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[2]>0:
							# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[11]<=1.0:
								return 'True'
							elif obj[11]>1.0:
								return 'False'
							else: return 'False'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[5]>0:
						return 'True'
					else: return 'True'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	elif obj[9]>10:
		# {"feature": "Education", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[8]<=4:
			# {"feature": "Bar", "instances": 15, "metric_value": 0.5665, "depth": 3}
			if obj[11]>0.0:
				return 'False'
			elif obj[11]<=0.0:
				# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[0]>0:
					# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[7]<=0:
						return 'True'
					elif obj[7]>0:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[8]>4:
			return 'True'
		else: return 'True'
	else: return 'False'
