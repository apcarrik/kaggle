def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[2]>0:
		# {"feature": "Restaurant20to50", "instances": 42, "metric_value": 0.9587, "depth": 2}
		if obj[12]<=2.0:
			# {"feature": "Education", "instances": 37, "metric_value": 0.9868, "depth": 3}
			if obj[7]<=2:
				# {"feature": "Time", "instances": 29, "metric_value": 0.9294, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Direction_same", "instances": 24, "metric_value": 0.9799, "depth": 5}
					if obj[13]<=0:
						# {"feature": "Coupon_validity", "instances": 20, "metric_value": 1.0, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[8]<=6:
								return 'True'
							elif obj[8]>6:
								# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[3]>0:
							# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[11]>0.0:
								return 'False'
							elif obj[11]<=0.0:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[0]>1:
									return 'True'
								elif obj[0]<=1:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[13]>0:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[7]>2:
				# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[5]>2:
					return 'False'
				elif obj[5]<=2:
					# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[11]>1.0:
						return 'True'
					elif obj[11]<=1.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[12]>2.0:
			return 'True'
		else: return 'True'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
