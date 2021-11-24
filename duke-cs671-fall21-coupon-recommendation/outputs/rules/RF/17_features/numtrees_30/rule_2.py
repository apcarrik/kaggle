def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Weather", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Coupon", "instances": 31, "metric_value": 0.9383, "depth": 2}
		if obj[3]>0:
			# {"feature": "Occupation", "instances": 26, "metric_value": 0.8404, "depth": 3}
			if obj[10]<=16:
				# {"feature": "Coupon_validity", "instances": 21, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=0:
					# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[9]<=2:
						return 'True'
					elif obj[9]>2:
						# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[12]>1.0:
							return 'False'
						elif obj[12]<=1.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[4]>0:
					# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[13]<=1.0:
						# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[5]>0:
							return 'False'
						elif obj[5]<=0:
							return 'True'
						else: return 'True'
					elif obj[13]>1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[10]>16:
				return 'True'
			else: return 'True'
		elif obj[3]<=0:
			# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[9]<=2:
				return 'False'
			elif obj[9]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]>1:
		return 'False'
	else: return 'False'
