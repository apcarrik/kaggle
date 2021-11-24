def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9367, "depth": 1}
	if obj[17]<=2:
		# {"feature": "Coffeehouse", "instances": 70, "metric_value": 0.8435, "depth": 2}
		if obj[13]>0.0:
			# {"feature": "Education", "instances": 56, "metric_value": 0.7147, "depth": 3}
			if obj[9]>1:
				# {"feature": "Direction_same", "instances": 31, "metric_value": 0.8691, "depth": 4}
				if obj[16]<=0:
					# {"feature": "Passanger", "instances": 20, "metric_value": 0.971, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Coupon_validity", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[4]<=0:
							# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[12]>1.0:
								return 'True'
							elif obj[12]<=1.0:
								# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[10]<=12:
									return 'False'
								elif obj[10]>12:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]>0:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[16]>0:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[10]>2:
						return 'True'
					elif obj[10]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[9]<=1:
				# {"feature": "Bar", "instances": 25, "metric_value": 0.4022, "depth": 4}
				if obj[12]<=3.0:
					# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.2499, "depth": 5}
					if obj[15]>0.0:
						return 'True'
					elif obj[15]<=0.0:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]>1:
							return 'True'
						elif obj[3]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[12]>3.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[13]<=0.0:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Restaurantlessthan20", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[14]>1.0:
					return 'True'
				elif obj[14]<=1.0:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]>3:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[17]>2:
		# {"feature": "Coupon_validity", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[4]>0:
			# {"feature": "Bar", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[12]<=0.0:
				# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[2]<=1:
					return 'True'
				elif obj[2]>1:
					return 'False'
				else: return 'False'
			elif obj[12]>0.0:
				return 'False'
			else: return 'False'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
