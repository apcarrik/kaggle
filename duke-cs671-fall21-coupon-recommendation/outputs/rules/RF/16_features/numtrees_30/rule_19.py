def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Time", "instances": 28, "metric_value": 0.9666, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Children", "instances": 20, "metric_value": 0.8113, "depth": 3}
			if obj[7]<=0:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[3]>0:
					return 'True'
				elif obj[3]<=0:
					# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>0:
						return 'True'
					elif obj[4]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]>0:
				# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[13]>0.0:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[3]<=3:
						# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[8]>2:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[15]<=2:
								return 'False'
							elif obj[15]>2:
								return 'True'
							else: return 'True'
						elif obj[8]<=2:
							return 'True'
						else: return 'True'
					elif obj[3]>3:
						return 'True'
					else: return 'True'
				elif obj[13]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]>2:
			# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[9]>1:
				return 'False'
			elif obj[9]<=1:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>0:
					return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
