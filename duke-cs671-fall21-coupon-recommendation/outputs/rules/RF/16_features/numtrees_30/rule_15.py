def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[3]>1:
		# {"feature": "Weather", "instances": 26, "metric_value": 0.9306, "depth": 2}
		if obj[1]<=0:
			# {"feature": "Education", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[8]<=3:
				# {"feature": "Bar", "instances": 18, "metric_value": 1.0, "depth": 4}
				if obj[11]>0.0:
					# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[12]<=3.0:
						# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[13]>0.0:
							# {"feature": "Gender", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[13]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[12]>3.0:
						return 'False'
					else: return 'False'
				elif obj[11]<=0.0:
					# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=5:
							return 'True'
						elif obj[6]>5:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[8]>3:
				return 'True'
			else: return 'True'
		elif obj[1]>0:
			return 'True'
		else: return 'True'
	elif obj[3]<=1:
		return 'False'
	else: return 'False'
