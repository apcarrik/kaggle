def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Age", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[6]<=3:
		# {"feature": "Coffeehouse", "instances": 30, "metric_value": 0.9183, "depth": 2}
		if obj[13]>0.0:
			# {"feature": "Bar", "instances": 23, "metric_value": 0.9877, "depth": 3}
			if obj[12]<=1.0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[10]<=6:
					# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[2]>0:
						# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[9]<=0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						elif obj[9]>0:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[10]>6:
					return 'True'
				else: return 'True'
			elif obj[12]>1.0:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[8]<=0:
						return 'True'
					elif obj[8]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[13]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[6]>3:
		# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.8631, "depth": 2}
		if obj[13]<=1.0:
			# {"feature": "Time", "instances": 12, "metric_value": 1.0, "depth": 3}
			if obj[2]>0:
				# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[12]<=0.0:
					return 'False'
				elif obj[12]>0.0:
					# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>0:
						return 'True'
					elif obj[4]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3]>0:
					return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[13]>1.0:
			return 'True'
		else: return 'True'
	else: return 'True'
