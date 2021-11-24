def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[13]<=2.0:
		# {"feature": "Coffeehouse", "instances": 29, "metric_value": 0.9294, "depth": 2}
		if obj[12]<=3.0:
			# {"feature": "Education", "instances": 27, "metric_value": 0.8767, "depth": 3}
			if obj[8]<=3:
				# {"feature": "Age", "instances": 24, "metric_value": 0.9183, "depth": 4}
				if obj[6]>3:
					# {"feature": "Time", "instances": 14, "metric_value": 0.7496, "depth": 5}
					if obj[2]<=1:
						return 'False'
					elif obj[2]>1:
						# {"feature": "Children", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[7]<=0:
							# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[9]<=12:
								return 'True'
							elif obj[9]>12:
								return 'False'
							else: return 'False'
						elif obj[7]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[6]<=3:
					# {"feature": "Time", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[2]<=1:
						# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[1]<=0:
							return 'True'
						elif obj[1]>0:
							return 'False'
						else: return 'False'
					elif obj[2]>1:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[9]>1:
							return 'False'
						elif obj[9]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[8]>3:
				return 'False'
			else: return 'False'
		elif obj[12]>3.0:
			return 'True'
		else: return 'True'
	elif obj[13]>2.0:
		return 'True'
	else: return 'True'
